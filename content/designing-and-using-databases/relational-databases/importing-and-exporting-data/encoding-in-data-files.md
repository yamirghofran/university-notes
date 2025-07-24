---
title: Encoding in Data Files
---

# ASCII (American Standard Code for Information Interchange)
- ASCII is an older character encoding standard that uses 7 bits to represent 128 different characters.
- It's limited to the basic Latin alphabet, numbers, punctuation, and control characters.
- ASCII is not suitable for encoding characters from non-Latin scripts.

# UTF-8 (Unicode Transformation Format-8)
- UTF-8 is a variable-width character encoding capable of representing all Unicode characters.
- It's backward-compatible with ASCII, meaning the first 128 characters in UTF-8 are the same as in ASCII.
- UTF-8 is widely used for web content, data exchange, and storage as it supports a wide range of languages.

# UTF-16 (Unicode Transformation Format-16)
- UTF-16 is another encoding for Unicode characters, using 16 bits per character.
- It can represent a broader range of characters compared to UTF-8.
- UTF-16 is commonly used in systems that require extensive character support but results in larger file sizes due to the use of 16 bits per character.

# Difference between encoding and its impact

| Encoding  | Character Range                                                                                | File Size          | Compatibility                                                       | Human-Readability                         |
| --------- | ---------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------- | ----------------------------------------- |
| **ASCII** | Limited to the basic Latin characters                                                          | Smaller file sizes | Limited to basic characters, not suitable for multilingual content. | Simplest to read bc limited character set |
| **UTF-8** | Supports a much broader range of characters, including non-Latin scripts, symbols, and emojis. | Larger file sizes  | Compatibility with ASCII and broad support for different languages. | Can be human-readable                     |
