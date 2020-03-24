# NPM
[A Beginners Guide](https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/)


## package.json
- A file that can described as a manafest of the project that includes the packages and applications that your project depends on, infromation about it's unique sorce control and spesific metadata like the projects name, description and auther.

### Metadata
This metadata helps identify the project and acts as a baseline for users and contributors to get information about the project.

```json
{
  "name": "metaverse", // The name of your project
  "version": "0.92.12", // The version of your project
  "description": "The Metaverse virtual reality. The final outcome of all virtual worlds, augmented reality, and the Internet.", // The description of your project
  "main": "index.js"
  "license": "MIT" // The license of your project
}
```
`package.json` files can be genereated with the `npm init` comand

### Understanding your projects dependancies and devDependencies
The majory important aspect of the `package.json` file is 