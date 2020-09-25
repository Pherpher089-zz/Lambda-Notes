# Getting Started

## Install Sass

Using this [link](https://sass-lang.com/install), follow the directions to install sass if it has not been already

## 2. Basic Precompile

Create a `style.css` and `style.sass`. Once the code has been written in the `style.sass` file, run the following command to precompile the `sass` into `css`:

> sass index.sass:index.css

This complies one file into another but definitely not supper efficient.

## Set the watch compiler

In order for the precompiler to update your `css` file with all of the code in the `sass` file, you need to set the pre compiler to watch your `sass` file. adding the `--watch` parameter in the command will do just that.

    > sass --watch style.sass:style.css

## A note about syntax
- There are no brackets or semicolons. Line endings are returns.
- You can nest selectors
- Variables start with a '$'
- To define a mixin use the '='
```sass
=Mixin($color)
    property: $color
    property: value
```
- To add a mixin, use the  '+'. example:
```sass
div
    +Mixin(red)
```

## Partials and imports
A partial is a separate sass file that that is a part of the main sass file. These files are all named starting with an underscore. These files can be tied or imported to the main sass file with an import statement. The rules of specificity sill apply so its good to remember that the import is just like that file and all its code appearing on the line it was imported on.

## Selector Inheritance and Operators 
Selector inheritance is similar to using mixins. The key difference is that there are no parameters with inherited selectors. They work like this:

1) define the selector class
```sass
%newSelector
    property:value
    property:value
```

2) add it in to an existing class
```sass
.OtherClass
    @extend %newSelector
```
