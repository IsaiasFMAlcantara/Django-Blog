# [<-](https://github.com/IsaiasFMAlcantara/Django-Blog) Passo a passo Git
1. Criar repositório local
    ```sh
    git init
    ```
1. Adicionar todo seu projeto na branch local
    ```sh
    git add .
    ```
1. Commitar tudo que você adicionou na branch no repositório local
    ```sh
    git commit -m "seu comentario"
    ```
1. Validar qual nome da sua branch local
    ```sh
    git branch
    ```
1. Mudar nome da branch para main (opicional)
    ```sh
    git branch -M main
    ```
1. Adicionar repositório externo
    ```sh
    git remote add origin seu link
    ```
1. Validar se foi criado
    ```sh
    git remote
    ```
1. Comitar no reporitório externo (main caso você renomeie sua branch para main)
    ```sh
    git push -uf origin main
    ```