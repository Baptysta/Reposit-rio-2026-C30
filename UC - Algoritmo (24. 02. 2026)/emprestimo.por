programa{
    funcao inicio(){
        real preco, salario, parcela, porcento
        inteiro anos, meses

        escreva("Qual o valor do imóvel?")
        leia(preco)

        escreva("Digite o valor do salário mensal do comprador")
        leia(salario)

        escreva("Digite em quantos anos o comprador pretende quitar o imóvel")
        leia(anos)

        parcela = preco / anos

        porcento = salario * 0.3

        se(parcela >= porcento){
            escreva("Parcelas de", parcela," mensais; Emprestimo negado, o valor exede 30% do salário do comprador")
        }senao{
            escreva("Parcelas de", parcela,"mensais; Emprestimo aprovado")

        }


    }
}