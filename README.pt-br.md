# whvn<i>.py</i>
![preview](https://raw.githubusercontent.com/F4Jonatas/whvn/main/img/preview.png)
<br>

[![donate](https://img.shields.io/badge/$-donate-ff69b4.svg?style=for-the-badge)](https://www.buymeacoffee.com/jonatasp3)

## Descrição
Este é um projeto desenvolvido no intuito de impulsionar o uso de um dos melhores sites já feitos para wallpapers.
Como uso o [Wallhaven](https://wallhaven.cc/) desde sua primeira aparição, continuação do também amado [Wallbase](https://wallhaven.cc/w/4vd1m4), não hà nada melhor do que [_espalhar a palavra_](https://wallhaven.cc/faq#What-can-I-do-to-help-out).
Também tive como inspiração [Wallhaven API for Python](https://github.com/Goblenus/WallhavenApi).

Costumo usar com [PowerShell Core](https://github.com/PowerShell/PowerShell) (Windows) ou [Termux](https://termux.dev/en/) (Android). Também faço testes no [Deepin](https://www.deepin.org/index/en) (Linux), mas nele não consigo mudar o wallpaper do meu desktop, caso alguém consiga nos ajudar, ficarei muito grato! :blush:

Agora estou me concentrando em outros projetos e posso levar algum tempo para atender a novas atualizações. Esteja à vontade para adicionar soluções.

---

## Documentação rápida
#### Importação do arquivo e do módulo whvn:
``` python
from whvn import whvn, support
```
<details><summary><strong>Saber mais</strong></summary>

| Classe | Descrição |
| :--- | :---: |
| `whvn` | O primordial, onde se encontra as funções para acessar nosso querido site. |
| `support` | Uma classe secundária, que contém funções para baixar e mudar o nosso wallpaper. |
</details>

---


#### Inicialize o módulo:
``` python
wh = whvn(
	# user   [string/optional],
	# apikey [string/optional]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `user` | Para obter coleções de wallpaper. |
| `apikey` | Se uma [chave de API](https://wallhaven.cc/help/api#auth) for fornecida, você concederá mais privilégios.<br>Para acessar suas configurações ou os papéis de parede [NSFW](https://wallhaven.cc/rules#Purity), isso é necessário. |
</details>

---


#### Pesquisa e listagens:
``` python
db = wh.search(
	# id          [string/integer/optional],
	# like        [string/optional],
	# user        [string/optional],
	# query       [string/list/tuple/optional],
	# exclude     [string/list/tuple/optional],
	# page        [string/integer/optional],
	# atleast     [string/optional],
	# ratios      [string/optional],
	# category    [string/optional],
	# purity      [string/optional],
	# resolutions [string/optional],
	# toprange    [string/optional],
	# colors      [string/optional],
	# sorting     [string/optional],
	# order       [string/optional],
	# seed        [string/optional]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `id` | Pesquisa exata de tags.<br>Não pode ser combinado com `like/query/exclude`. |
| `like` | Encontre wallpapers com tags semelhantes.<br>Não pode ser combinado com `id/query/exclude`. |
| `user` | Encontrar uploads de usuários. |
| `query` | Pesquise vagamente por uma tag/palavra-chave.<br>Não pode ser combinado com `like/id`. |
| `exclude` | Excluir uma tag/palavra-chave.<br>Não pode ser combinado com `like/id`. |
| `page` | Número de paginação. |
| `atleast` | Resolução mínima permitida. |
| `ratios` | Lista de proporções de aspecto. |
| `category` | Categorias `general/anime/people`.<br>Ativar categorias (1) ou desativar (0).<br>Padrão `111`. |
| `purity` | [Purezas](https://wallhaven.cc/rules#Purity) `sfw/sketchy/nsfw`. NSFW requer uma [chave de API](https://wallhaven.cc/help/api#auth).<br>Ativar categorias (1) ou desativar (0).<br>Padrão `100`. |
| `resolutions` | [Resolução](https://screenresolutiontest.com/) exata do wallpaper. |
| `toprange` | Organiza a lista principal.<br>O parâmetro `sorting` deve ser definida como `toplist`.<br>Padrão `1M`. |
| `colors` | Busca por [cor hexadecimal](https://www.color-hex.com/). |
| `sorting` | Método de classificação dos resultados.<br>Ele não o contém no [API original](https://wallhaven.cc/help/api), mas você também pode usar o valor `hot`.<br>Padrão `date_added`. |
| `order` | Ordem de classificação.<br>Padrão `desc`. |
| `seed` | Semente opcional para resultados aleatórios. |
</details>

---


#### Informações da etiqueta:
``` python
db = wh.taginfo(
	# tagid [string/integer/required]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `tagid` | Obtenha mais informações sobre a etiqueta.<br>ID é encontrada na [URL da etiqueta](https://wallhaven.cc/tag/323), ou você também pode usar a URL completa. |
</details>

---


#### Informações do wallpaper:
``` python
db = wh.info(
	# wallid [string/required]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `wallid` | Obtenha mais informações do wallpaper.<br>ID é encontrada na [URL da imagem](https://wallhaven.cc/w/9m92rx), ou você também pode usar a URL completa.<br>Os papéis de parede NSFW são bloqueados para os convidados. Os usuários podem acessá-los fornecendo sua [chave de API](https://wallhaven.cc/help/api#auth). |
</details>

---


#### Coleções de usuários:
``` python
db = wh.collection(
	# user   [string/required]
	# full   [boolean/optional]
	# foldid [string/integer/optional]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `user` | Nome do usuário para pesquisa. |
| `full` | Use para obter toda a coleção, incluindo informações do wallpaper.<br>Padrão `False`. |
| `foldid` | Usar para obter a coleção de uma determinada pasta. |
</details>

---


#### Wallpaper ou pasta aleatória:
``` python
wall = wh.random(
	# data [dict/required]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `data` | Valor retornado pelo método `whvn.collection` ou `whvn.search`. |
</details>

---


#### Configurações do usuário:
``` python
db = wh.settings(
	# apikey [string/optional]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `apikey` | Para acessar suas configurações, se você não tiver passado ao [iniciar o módulo](https://github.com/F4Jonatas/whvn#initialize-the-module), isto é necessário. |
</details>

---


#### Baixando o wallpaper:
``` python
file = support.download(
	# uri     [string/dict/required]
	# imgname [string/optional]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `uri` | [URL da imagem](https://wallhaven.cc/w/9m92rx) ou informação do wallpaper `(dict)`, obtida com `whvn.collection` ou `whvn.search`, para download. |
| `imgname` | Nome e extensão para a imagem.<br>É baixado no mesmo diretório do script.<br>Padrão `whvn.png`. |
</details>

---


#### Mudando o wallpaper:
``` python
file = support.setwall(
	# file [string/required]
	# cmd  [string/optional]
)
```
<details><summary><strong>Saber mais</strong></summary>

| Parâmetro | Descrição |
| --- | --- |
| `file` | Caminho da imagem, devolvido pelo método `support.download`. |
| `cmd` | Definir o wallpaper para ambiente Linux.<br>Como mencionei a cima, eu não consigo utilizar, mas criei esta possibilidade para quem consiga usar ou modificar.<br>A solução pode ser encontrada no [pywal](https://github.com/dylanaraps/pywal/blob/master/pywal/wallpaper.py). |
</details>

---

## Doação
[![buymeacoffee](https://raw.githubusercontent.com/F4Jonatas/whvn/main/img/donate.webp)](https://www.buymeacoffee.com/jonatasp3)
<br>
Se gostou do meu pequeno trabalho, não deixe de mostrar isso.<br>
_"Doar é um ato emocional, reconhecimento."_

---


## Licença
> **Licença Pública Geral GNU v2.0**<br>
> A GNU GPL é a licença de software livre mais amplamente utilizada e tem um forte requisito de copyleft. Ao distribuir obras derivadas, o código fonte da obra deve ser disponibilizado sob a mesma licença.
