# Styling with CSS

'Cascading Style Sheets'

## Height and width properties

The `height` and `width` properties are used to set the height and width of an element.

The height and width properties do not include padding, borders, or margins. It sets the height/width of the area inside the padding, border, and margin of the element.

### CSS height and width Values

The `height` and `width` properties may have the following values:

-   `auto` - This is default. The browser calculates the height and width
-   `length` - Defines the height/width in px, cm etc.
-   `%` - Defines the height/width in percent of the containing block
-   `initial` - Sets the height/width to its default value
-   `inherit` - The height/width will be inherited from its parent value

#### Setting the max-width property

The `max-width` property is used to set the maximum width of an element.

# CSS GRID

1. set the parent element display to grid

```css
.containerClass {
	display: grid;
}
```

2. Set the spacing for the columns or rows

```css
.containerClass {
	display: grid;
	grid-template-columns: 1fr;
	grid-template-rows: 1fr;
}
```

These values can be set to any graduation including px, rem, %, vw, etc... The `fr` unit is a fraction of the space. This takes into account all of the `fr` units that are in the row or column and creates a spacing that reflects the fractions in the space.

Using `repeat()` as a value for the template, you can specify how many times to repeat and then the unit to repeat

```css
.containerClass {
	display: grid;
	grid-template-columns: repeat(4, 1fr);
	grid-template-rows: 1fr;
}
```

**Sub Grids** are achieved by marking the display property of a grid element as grid. All of its children will follow the rules set by their parent, within the grid space of their parent

`grid column` and `grid-row` are values that can specify the amount of space that one cell can take up. For instance setting the `grid-column` to 1/3 will stretch this particular cell from the first column line to the third column line.
