# whvn<i>.py</i>
![preview](https://raw.githubusercontent.com/F4Jonatas/whvn/main/img/preview.png)
<br>

[![donate](https://img.shields.io/badge/$-donate-ff69b4.svg?style=for-the-badge)](https://www.buymeacoffee.com/jonatasp3)

## Description
This is a project developed in order to promote the use of one of the best sites ever made for wallpapers. Since I use [Wallhaven](https://wallhaven.cc/) since its first appearance, a continuation of the also beloved [Wallbase](https://wallhaven.cc/w/4vd1m4), there is nothing better than [spreading the word](https://wallhaven.cc/faq#What-can-I-do-to-help-out).<br>
I also took [Wallhaven API for Python](https://github.com/Goblenus/WallhavenApi) as inspiration.

I usually use it with [PowerShell Core](https://github.com/PowerShell/PowerShell) (Windows) or [Termux](https://termux.dev/en/) (Android). I also do tests on [Deepin](https://www.deepin.org/index/en) (Linux), but on it I can't change my desktop wallpaper, if anyone can help us, I will be very grateful! :blush:

I am now concentrating on other projects and may take some time to attend to new updates. Feel free to add solutions.

---

## Quick documentation
#### Importing the whvn file and module:
``` python
from whvn import whvn, support
```
<details><summary><strong>Learn More</strong></summary>

| Class | Description |
| :--- | :---: |
| `whvn` | The primordial, where you find the functions to access our beloved site. |
| `support` | A secondary class, which contains functions for downloading and changing our wallpaper. |
</details>

---


#### Initialize the module:
``` python
wh = whvn(
	# user   [string/optional],
	# apikey [string/optional]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `user` | To get wallpaper collections. |
| `apikey` | If an [API key](https://wallhaven.cc/help/api#auth) is provided, you will grant it more privileges.<br>To access your settings or the [NSFW](https://wallhaven.cc/rules#Purity) wallpapers, this is required. |
</details>

---


#### Search and listings:
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
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `id` | Exact tag search.<br>Cannot be combined with `like/query/exclude`. |
| `like` | Find wallpapers with similar tags.<br>Cannot be combined with `id/query/exclude`. |
| `user` | Find user uploads. |
| `query` | Search fuzzily for a tag/keyword.<br>Cannot be combined `with like/id`. |
| `exclude` | Exclude a tag/keyword..<br>Cannot be combined with `like/id`. |
| `page` | Pagination number. |
| `atleast` | Minimum allowed resolution. |
| `ratios` | List of aspect ratios. |
| `category` | Categories `general/anime/people`.<br>Enable categories (1) or disable (0).<br>Default `111`. |
| `purity` | [Purity](https://wallhaven.cc/rules#Purity) `sfw/sketchy/nsfw`. NSFW requires an [API key](https://wallhaven.cc/help/api#auth).<br>Enable categories (1) or disable (0).<br>Default `100`. |
| `resolutions` | Exact [resolution](https://screenresolutiontest.com/) of the wallpaper. |
| `toprange` | Sorts the main list.<br>The `sorting` parameter must be set to `toplist`.<br>Default `1M`. |
| `colors` | Search by [hexadecimal color](https://www.color-hex.com/). |
| `sorting` | Method for sorting the results.<br>It does not contain it in the [original API](https://wallhaven.cc/help/api), but you can also use the `hot` value.<br>Default `date_added`. |
| `order` | Sort order.<br>Default `desc`. |
| `seed` | Optional seed for random results. |
</details>

---


#### Tag Information:
``` python
db = wh.taginfo(
	# tagid [string/integer/required]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `tagid` | Get more information about the tag.<br>ID is found in the [tag URL](https://wallhaven.cc/tag/323), or you can also use the full URL. |
</details>

---


#### Wallpaper Information:
``` python
db = wh.info(
	# wallid [string/required]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `wallid` | Get more information of the wallpaper.<br>ID is found in the [image URL](https://wallhaven.cc/w/9m92rx), or you can also use the full URL.<br>NSFW wallpapers are blocked for guests. Users can access them by providing their [API key](https://wallhaven.cc/help/api#auth). |
</details>

---


#### User Collections:
``` python
db = wh.collection(
	# user   [string/required]
	# full   [boolean/optional]
	# foldid [string/integer/optional]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `user` | User name for search. |
| `full` | Use to get the entire collection, including wallpaper information.<br>Default `False`. |
| `foldid` | Use to get the collection for a particular folder. |
</details>

---


#### Wallpaper or random folder:
``` python
wall = wh.random(
	# data [dict/required]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `data` | Value returned by the `whvn.collection` or `whvn.search` method. |
</details>

---


#### User Settings:
``` python
db = wh.settings(
	# apikey [string/optional]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `apikey` | To access your settings, if you have not passed when starting the module, this is required. |
</details>

---


#### Wallpaper download:
``` python
file = support.download(
	# uri     [string/dict/required]
	# imgname [string/optional]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `uri` | [Image URL](https://wallhaven.cc/w/9m92rx) or wallpaper information `(dict)`, obtained with `whvn.collection` or `whvn.search`, for download. |
| `imgname` | Name and extension for the image.<br>It is downloaded in the same directory as script.<br>Default `whvn.png`. |
</details>

---


#### Changing the wallpaper:
``` python
file = support.setwall(
	# file [string/required]
	# cmd  [string/optional]
)
```
<details><summary><strong>Learn More</strong></summary>

| Parameter | Description |
| --- | --- |
| `file` | Path of the image, returned by the `support.download method`. |
| `cmd` | Setting the wallpaper for Linux environment.<br>As I mentioned above, I can't use it, but I created this possibility for those who can use or modify it.<br>The solution can be found in [pywal](https://github.com/dylanaraps/pywal/blob/master/pywal/wallpaper.py). |
</details>

---

## Donation
[![buymeacoffee](https://media0.giphy.com/media/o7RZbs4KAA6tvM4H6j/200w.webp)](https://www.buymeacoffee.com/jonatasp3)
<br>
If you enjoyed my little work, be sure to show it off.<br>
_"Donation is an emotional act, recognition."_

---


## License
> **GNU General Public License v2.0**<br>
> The GNU GPL is the most widely used free software license and has a strong copyleft requirement. When distributing derivative works, the source code of the work must be made available under the same license.
