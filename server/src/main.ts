import https from "https";
import configs from "./configs/index.js";
import httpsOptions from "./configs/certificate.js";
import { expressApp } from "./express/index.js";


// -------- Start Server --------

const server = https.createServer(httpsOptions, expressApp);
const { MAIN_IP, PORT_BACK } = configs;
server.listen(PORT_BACK, () => {
  console.log("====== SERVER RUNNING ======");
  console.log(` - https://${MAIN_IP}:${PORT_BACK}`);
});
