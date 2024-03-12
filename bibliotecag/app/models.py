from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length = 100)
    uf = models.CharField(max_length = 2)

    def __str__(self):
        return f'{self.nome, self.uf}'

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome , self.email}'
    
class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    site = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome, self.cidade, self.site}'
    
class Autor(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.cidade, self.nome}'

class Livro(models.Model):
    editora = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits= 10, decimal_places=2)
    datapublicacao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.editora, self.autor, self.genero, self.nome, self.preco, self.datapublicacao}'

class EmprestimoLivro(models.Model):
    livro = models.CharField(max_length=100)
    leitor = models.CharField(max_length=100)
    dataemprestimo = models.DateField()
    datadevolucao = models.DateField()

    def __str__(self):
        return f'{self.livro, self.leitor, self.dataemprestimo, self.datadevolucao}'