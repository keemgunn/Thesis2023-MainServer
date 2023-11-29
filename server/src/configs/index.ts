import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const OS_TYPE = (process.platform === 'win32') ? 'win' : 'mac';

let configsFile;
try {
  console.log("... Loading configs file");
  let fileContents;
  if (OS_TYPE === 'win') {
    fileContents = fs.readFileSync(path.resolve(__dirname, '../../../configs/Windows/configs.yml'), 'utf8');
  } else {
    fileContents = fs.readFileSync(path.resolve(__dirname, '../../../configs/MacOS/configs.yml'), 'utf8');
  }
  configsFile = yaml.load(fileContents);
  
  console.log("... Successfully loaded configs file!");
} catch (e) {
  console.error(e);
}

const configs: any = {
  ...configsFile as any,
  OS_TYPE,
};
console.log(configs);

export default configs;