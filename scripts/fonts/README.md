# Bundled PDF fonts

Noto Serif CJK SC, Regular and Bold, under the SIL Open Font License 1.1 (see `OFL.txt`). These complete Simplified Chinese fonts are bundled as WOFF2 so PDF builds work offline and do not depend on an installed Chinese font. Chromium embeds the used glyphs in the PDF. This directory is excluded from the website along with `scripts/`.

Upstream sources (downloaded 10 October 2026):

- https://github.com/notofonts/noto-cjk/blob/main/Serif/SubsetOTF/SC/NotoSerifSC-Regular.otf
- https://github.com/notofonts/noto-cjk/blob/main/Serif/SubsetOTF/SC/NotoSerifSC-Bold.otf
- https://github.com/notofonts/noto-cjk/blob/main/Serif/LICENSE

Converted losslessly with FontTools 4.60.1 and Brotli 1.2.0 by loading each OTF with `TTFont`, setting `font.flavor = 'woff2'`, and calling `font.save(...)`. No glyph subsetting or font-design changes were made. FontTools is only needed to replace these bundled assets, not for normal CV builds.
