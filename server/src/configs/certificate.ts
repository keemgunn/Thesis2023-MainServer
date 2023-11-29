import https from 'https';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const keyFilePath: string = (process.platform === 'win32') ? '../../../configs/Windows/certificates/cert-key.pem' : '../../../configs/MacOS/certificates/cert-key.pem';
const certFilePath: string = (process.platform === 'win32') ? '../../../configs/Windows/certificates/fullchain.pem' : '../../../configs/MacOS/certificates/fullchain.pem';

console.log('... Loading certificate files');
const key = fs.readFileSync(path.resolve(__dirname, keyFilePath));
const cert = fs.readFileSync(path.resolve(__dirname, certFilePath));

if (key && cert) {
  console.log('... Successfully loaded certificate files!');
}

const httpsOptions = {
  key, cert
} satisfies https.ServerOptions;

export default httpsOptions;