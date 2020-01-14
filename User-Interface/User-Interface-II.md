# User Interface II
*Box Model*,
*Positioning*,
*CSS Reset*

## Box Model
1. Margin
	* The area between other elements and this element
2. Border
	* A border that we can style around the padding and content of a box
3. Padding
	* The space between the content and the border
4. Content
	* This is where text and images are rendered

## Positioning

Here is a cool [Code Pen](https://codepen.io/Pherpher089/pen/gyqjvZ?editors=0100) that demonstrates how relative and absolute positioning works


## CSS Resets

## Eric Meyer Reset
```CSS
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
```

## Global Less Reset
```LESS
/**
 * Global Reset of all HTML Elements
 *
 * Resetting all of our HTML Elements ensures a smoother
 * visual transition between browsers. If you don't believe me,
 * try temporarily commenting out this block of code, then go
 * and look at Mozilla versus Safari, both good browsers with
 * a good implementation of CSS. The thing is, all browser CSS
 * defaults are different and at the end of the day if visual
 * consistency is what we're shooting for, then we need to
 * make sure we're resetting all spacing elements.
 *
 */
html, body {
	border: 0;
	font-family: "Helvetica-Neue", "Helvetica", Arial, sans-serif;
	line-height: 1.5;
	margin: 0;
	padding: 0;
}

div, span, object, iframe, img, table, caption, thead, tbody,
tfoot, tr, tr, td, article, aside, canvas, details, figure, hgroup, menu,
nav, footer, header, section, summary, mark, audio, video {
  border: 0;
  margin: 0;
  padding: 0;
}

h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, address, cit, code,
del, dfn, em, ins, q, samp, small, strong, sub, sup, b, i, hr, dl, dt, dd,
ol, ul, li, fieldset, legend, label {
  border: 0;
  font-size: 100%;
  vertical-align: baseline;
  margin: 0;
  padding: 0;
}

article, aside, canvas, figure, figure img, figcaption, hgroup,
footer, header, nav, section, audio, video {
	display: block;
}

table {
  border-collapse: separate;
  border-spacing: 0;
  caption, th, td {
    text-align: left;
    vertical-align: middle;
  }
}

a img {
  border: 0;
}

:focus {
  outline: 0;
}
```