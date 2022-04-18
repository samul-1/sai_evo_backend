const ts = require("typescript");
const tsConfig = require("./tsconfig.json");
const fs = require("fs");
const getRandomIdentifier = require("./utils").getRandomIdentifier;

function createTsSourceFile(filename, source) {
  fs.writeFileSync(filename, source);
  return filename;
}

function deleteTmpFiles(filename) {
  try {
    fs.unlinkSync(getAbsoluteTmpFilePath(filename) + ".ts");
    fs.unlinkSync(getAbsoluteTmpFilePath(filename) + ".js");
  } catch {}
}

function getAbsoluteTmpFilePath(filename) {
  return getTmpFileDir() + filename;
}

function getTmpFileDir() {
  return __dirname + "/tmp/";
}

function compile(source, options) {
  const filename = getRandomIdentifier(20);
  const filepath = getAbsoluteTmpFilePath(filename) + ".ts";

  if (!fs.existsSync(getTmpFileDir())) {
    fs.mkdirSync(getTmpFileDir(), 0744, { recursive: true });
  }

  createTsSourceFile(filepath, source);

  const defaultCompilerHost = ts.createCompilerHost({});
  const program = ts.createProgram([filepath], options, defaultCompilerHost);
  const emitResult = program.emit();

  const allDiagnostics = ts
    .getPreEmitDiagnostics(program)
    .concat(emitResult.diagnostics);

  const processedDiagnostics = allDiagnostics.map((diagnostic) => {
    if (diagnostic.file) {
      let { line, character } = ts.getLineAndCharacterOfPosition(
        diagnostic.file,
        diagnostic.start
      );
      let message = ts.flattenDiagnosticMessageText(
        diagnostic.messageText,
        "\n"
      );
      return `(on line ${line + 1}, at position ${character + 1}): ${message}`;
    } else {
      return ts.flattenDiagnosticMessageText(diagnostic.messageText, "\n");
    }
  });

  const res = {
    compilationErrors: processedDiagnostics,
  };

  if (processedDiagnostics.length === 0) {
    res.compiledCode = String(
      fs.readFileSync(getAbsoluteTmpFilePath(filename) + ".js")
    );
  }

  deleteTmpFiles(filename);
  return res;
}

const tsToJs = (source) => compile(source, tsConfig.compilerOptions);

module.exports = {
  tsToJs,
};
