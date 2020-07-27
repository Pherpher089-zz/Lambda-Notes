# Responsive Design II

## Prepare

### Resising text with em

em's are 1:10px. 1 em == 10px.

    body { font-size:62.5%; }
    h1 { font-size: 2.4em; } /* =24px */
    p  { font-size: 1.4em; } /* =14px */
    li { font-size: 1.4em; } /* =14px? */

Font size compounds with nested elements.

    body { font-size:62.5%; }
    h1 { font-size: 2.4em; } /* =24px */
    p  { font-size: 1.4em; } /* =14px */
    li { font-size: 1.4em; } /* =14px? */
    li li, li p /* etc */ { font-size: 1em; }

To avoid this issue, use rem's

    html { font-size: 62.5%; }
    body { font-size: 1.4rem; } /* =14px */
    h1   { font-size: 2.4rem; } /* =24px */

Making sure that older browsers are supported

    html { font-size: 62.5%; }
    body { font-size: 14px; font-size: 1.4rem; } /* =14px */
    h1   { font-size: 24px; font-size: 2.4rem; } /* =24px */

A basic and most common example: html font-size is set to 10px, paragraph is set to 1.6rem - 1.6rem \* 10px = 16px.

A typical method is to set the HTML font-size to 62.5%. That’s because 62.5% of 16px (typical default browser font-size) is 10px. That would still make 1.6rem = 16px. This now means that if the user’s default browser font-size is changed to, for example, 20px, 1.6rem would now equal 20px.
