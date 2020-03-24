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
The majory important aspect of the `package.json` file is the list of packages that your project depends on. These can be found under the `"dependencies"` key in the file. Runnning `npm install` or `yarn install` will install these node packages into your project. This helps prevent you from needing to bundle thes packages with your project.

Dependencies are added to the production version of your project. DevDependencies are only installed during development and will not be included in the production version of your project. 
```json
{
  "name": "metaverse",
  "version": "0.92.12",
  "description": "The Metaverse virtual reality. The final outcome of all virtual worlds, augmented reality, and the Internet.",
  "main": "index.js"
  "license": "MIT",
  "devDependencies": {
    "mocha": "~3.1",
    "native-hello-world": "^1.0.0",
    "should": "~3.3",
    "sinon": "~1.9"
  },
  "dependencies": {
    "fill-keys": "^1.0.2",
    "module-not-found-error": "^1.0.0",
    "resolve": "~1.1.7"
  }
}
```
One note to make is that `dependencies` and `devDependencies` are objects with key/value pares. The key is the name of the package and the value is the version of that package being used. 

### Esential npm Commands

#### npm init
This comand initalized your project with npm and will prompt you for the following information:
- project name
- inital version
- project description
- entry point (the projects main file)
- the test command (to trigger testing with something like `standard`)
- the projects git repo
- key words (tags related to the project)
- the projects license (the defalt is `ISC` most open source node projects are `MIT`)

`npm init` will just generate a the file in the current dir. It does nothing else. If the file needs to be moved to a different dir, it's completely safe to do so. 
```bash
npm init # This will trigger the initialization
```

#### npm init --yes
This will instantly initalize your project with out any prompts for information. This will be filled with default information.

**note** [npm tricks](https://nodesource.com/blog/eleven-npm-tricks-that-will-knock-your-wombat-socks-off)