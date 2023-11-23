import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const OS_TYPE = (process.platform === 'win32') ? 'win' : 'mac';

let configs;
try {
  console.log("... Loading configs file");
  let fileContents;
  if (OS_TYPE === 'win') {
    fileContents = fs.readFileSync(path.resolve(__dirname, '../../../configs/Windows/configs.yml'), 'utf8');
  } else {
    fileContents = fs.readFileSync(path.resolve(__dirname, '../../../configs/Windows/configs.yml'), 'utf8');
  }
  configs = yaml.load(fileContents);
  
  console.log("... Successfully loaded configs file!");
  console.log(configs);
} catch (e) {
  console.error(e);
}

export default {
  ...(configs as object),
  OS_TYPE,
};
