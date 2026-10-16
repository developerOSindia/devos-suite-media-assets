# DeveloperOS Media & Asset Processing Suite

[![Live App](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B.svg)](https://devos-media-assets.streamlit.app)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Ecosystem: DeveloperOS](https://img.shields.io/badge/Ecosystem-DeveloperOS-6366f1.svg)](https://developeros.in)
[![Tools Directory](https://img.shields.io/badge/Tools%20Directory-Online-10b981.svg)](https://toolkit.developeros.in)
[![Privacy: Client--Side](https://img.shields.io/badge/Privacy-Zero--Storage-10b981.svg)](https://developeros.in/privacy)
[![CI](https://github.com/developerOSindia/devos-suite-media-assets/actions/workflows/ci.yml/badge.svg)](https://github.com/developerOSindia/devos-suite-media-assets/actions)

Base64 image conversion, SVG code optimization, color palette generation, and aspect ratio math.

---

> 🚀 **Live Application**: [https://devos-media-assets.streamlit.app](https://devos-media-assets.streamlit.app)


## 🖥️ Interface Preview

```
┌─────────────────────────────────────────────────────────────┐
│ 🖼️ DeveloperOS Media & Asset Processing Suite               │
│ SVG Minifier | Base64 Image Encoder | Aspect Ratio Math     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🌟 Application Overview & Features

- **Client-Side & Offline-First**: All data is processed in-memory. Zero server logging or third-party telemetry.
- **Decoupled Business Logic**: Pure algorithm implementations isolated from the user interface.
- **DeveloperOS Design System**: Official styling, dark theme, and accessible contrast compliance.
- **Single-Click Exports**: Copy outputs directly to clipboard or download formatted artifacts.

---

## 🚀 Local Setup & Installation

### 1. Prerequisites
- Python 3.12+ (or modern browser/node runtime for web frontends)
- Standard development tools (`git`, `pip`)

### 2. Quickstart
```bash
# Clone the repository
git clone https://github.com/developerOSindia/devos-suite-media-assets.git
cd devos-suite-media-assets

# Install dependencies (if applicable)
pip install -r requirements.txt

# Run the local application
streamlit run app.py
```

---

## 🧪 Automated Testing

Run the automated test suite locally:
```bash
python3 -m unittest discover -s tests
```
Continuous integration runs on every push and pull request via GitHub Actions.

---

## 🚢 Deployment Guidelines

This project is configured for standalone deployment to:
**Streamlit Community Cloud (`https://media.toolkit.developeros.in`)**

For containerized environments, standard Dockerfiles and Compose configurations are supported.

---

## 🔒 Security & Privacy

This application processes all user input **strictly in-memory** with zero persistence:
- Read our full [Security Policy](SECURITY.md)
- For vulnerability reports, contact: **`security@developeros.in`**

---

## 🤝 Contributing

Contributions are warmly welcomed! Please read our [Contributing Guidelines](CONTRIBUTING.md) and check out open issues.

---

## 🏷️ Recommended GitHub Topics

When configuring this repository on GitHub, apply these topics:
`media-tools` `svg-optimizer` `base64-image` `color-palette` `aspect-ratio` `streamlit` `developeros`

---

## 📜 License & Ecosystem

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

- **Live Application**: [https://devos-media-assets.streamlit.app](https://devos-media-assets.streamlit.app)
- **Main Website**: [https://developeros.in](https://developeros.in)
- **Tools Portal**: [https://toolkit.developeros.in](https://toolkit.developeros.in)
- **GitHub Organization**: [https://github.com/developerOSindia](https://github.com/developerOSindia)