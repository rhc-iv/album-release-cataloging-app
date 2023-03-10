<h1 align="center">🎧 Album Release Cataloging App (ARCA)</h1>
<p align="center">
  <img alt="Language" src="https://img.shields.io/badge/language-python-blue"><br>
  <img alt="Python Version" src="https://img.shields.io/badge/python_version-3.11-yellow" /><br>
  <img alt="Version" src="https://img.shields.io/badge/app_version-1.10-blue.svg?cacheSeconds=2592000" />
  <p align="center">
  <a href="https://twitter.com/rhc_iv" target="_blank">
    <img alt="Twitter: rhc_iv" src="https://img.shields.io/twitter/follow/rhc_iv.svg?style=social" /><br>
  </a>
  <a href="https://mastodon.social/@rhciv1972" target="_blank">
    <img alt="Mastodon: rhciv1972" src="https://img.shields.io/mastodon/follow/109497169591319512?domain=https%3A%2F%2Fmastodon.social&style=social" />
  </a>
  </p>
</p>

### 🛋️ [Homepage](https://github.com/rhc-iv/album-release-cataloging-app)
---
> A Python app, built around the Tkinter module, that allows users to create a catalog of their personal music collection and store it to a .json file.


<p align="center">
  <img src="https://github.com/rhc-iv/album-release-cataloging-app/blob/main/screenshot.png" width="800" height="600" />
</p>

## 👩🏻‍💻 Usage

- Open the .py file in the editor/IDE of your choice and run the script!
- Use the _**Print**_ button to send the .json file output to console.
- Use the _**Add**_ button to add new information to the catalog.
- Use the _**Cancel**_ button to clear all catalog fields.
- Entries that appear in the app's _**TreeView**_ can be _**Updated**_ or _**Deleted**_.
- Use the _**Exit**_ button to exit the application.

## ⚠️ Caution

The **Streamlit** portion of this repository is unfinished. For now, it runs as a multipage app. I am mostly content with the _Add to the Catalog_ and _View the Catalog_ pages, but I am still working on the functionality of the _Search the Catalog_ page. I have both a `Submit` and a `Clear` button on the search page. Here, I want the `Clear` button to clear not only the catalog dataframe written to the window, but also whatever selections are being made in any of the dropdown menus. I suspect this will require more undertanding of the `st.session_state` method. For now, here are a few screenshots:
<p align="center">
  <img src="https://github.com/rhc-iv/album-release-cataloging-app/blob/main/screenshot02.png?raw=true" width="800" height="600">
</p>

## 📝 To-Do

- Work on TreeView readability.
- Add drop-down GUI element that allows users to select fields for catalog entries.
- Work on fleshing out the Streamlit app

## 👤 Author

 **Robert H. Carr, IV**

* Twitter: [@rhc_iv](https://twitter.com/rhc_iv)
* Github: [@rhc-iv](https://github.com/rhc-iv)
* Mastodon [@rhciv1972](https://mastodon.social/@rhciv1972)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/rhc-iv/album-release-cataloging-app/issues). 

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
