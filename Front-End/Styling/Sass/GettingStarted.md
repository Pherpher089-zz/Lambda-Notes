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
