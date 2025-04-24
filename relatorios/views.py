from django.shortcuts import render
from django.http import HttpResponse
from cadastros.models import Produto, Cliente
import io
from reportlab.pdfgen import canvas
import xlsxwriter

def relatorio(request):
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'relatorios/relatorio.html', {
        'produtos': produtos,
        'clientes': clientes,
    })

def export_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Relatório de Produtos e Clientes")
    y = 750
    p.drawString(50, y, "Produtos:")
    y -= 20
    for produto in Produto.objects.all():
        p.drawString(60, y, f"{produto.nome} - {produto.descricao} - R$ {produto.preco}")
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    y -= 20
    p.drawString(50, y, "Clientes:")
    y -= 20
    for cliente in Cliente.objects.all():
        p.drawString(60, y, f"{cliente.nome} - {cliente.email} - {cliente.telefone}")
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

def export_xls(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet1 = workbook.add_worksheet('Produtos')
    worksheet2 = workbook.add_worksheet('Clientes')

    # Write headers
    worksheet1.write(0, 0, 'Nome')
    worksheet1.write(0, 1, 'Descrição')
    worksheet1.write(0, 2, 'Preço')

    worksheet2.write(0, 0, 'Nome')
    worksheet2.write(0, 1, 'Email')
    worksheet2.write(0, 2, 'Telefone')

    # Write data
    row = 1
    for produto in Produto.objects.all():
        worksheet1.write(row, 0, produto.nome)
        worksheet1.write(row, 1, produto.descricao)
        worksheet1.write(row, 2, float(produto.preco))
        row += 1

    row = 1
    for cliente in Cliente.objects.all():
        worksheet2.write(row, 0, cliente.nome)
        worksheet2.write(row, 1, cliente.email)
        worksheet2.write(row, 2, cliente.telefone)
        row += 1

    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=relatorio.xlsx'
    return response
