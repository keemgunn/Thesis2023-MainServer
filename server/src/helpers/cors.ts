import configs from "../configs/index.js";
import type { CorsOptions } from "cors";
const { MAIN_IP } = configs as Configs;

const corsWhitelist: string[] = [];

corsWhitelist.push(`https://${MAIN_IP}:${configs.PORT_FRONT}`);
corsWhitelist.push(`http://${MAIN_IP}:${configs.PORT_FRONT}`);
corsWhitelist.push(`https://${MAIN_IP}:${configs.PORT_FRONT_DEV}`);
corsWhitelist.push(`http://${MAIN_IP}:${configs.PORT_FRONT_DEV}`);
corsWhitelist.push(`https://${MAIN_IP}:${configs.PORT_BACK}`);
corsWhitelist.push(`http://${MAIN_IP}:${configs.PORT_BACK}`);
corsWhitelist.push(`https://${MAIN_IP}:${configs.UNREAL_HTTP_PORT}`);
corsWhitelist.push(`http://${MAIN_IP}:${configs.UNREAL_HTTP_PORT}`);
corsWhitelist.push(`https://${MAIN_IP}:${configs.UNREAL_OSC_PORT}`);
corsWhitelist.push(`http://${MAIN_IP}:${configs.UNREAL_OSC_PORT}`);
corsWhitelist.push(`https://localhost:${configs.PORT_FRONT}`);
corsWhitelist.push(`http://localhost:${configs.PORT_FRONT}`);
corsWhitelist.push(`https://localhost:${configs.PORT_FRONT_DEV}`);
corsWhitelist.push(`http://localhost:${configs.PORT_FRONT_DEV}`);
corsWhitelist.push(`https://localhost:${configs.PORT_BACK}`);
corsWhitelist.push(`http://localhost:${configs.PORT_BACK}`);
corsWhitelist.push(`https://localhost:${configs.UNREAL_HTTP_PORT}`);
corsWhitelist.push(`http://localhost:${configs.UNREAL_HTTP_PORT}`);
corsWhitelist.push(`https://localhost:${configs.UNREAL_OSC_PORT}`);
corsWhitelist.push(`http://localhost:${configs.UNREAL_OSC_PORT}`);

console.log(`... CORS whitelist: \n${corsWhitelist}`);

export const corsOptions = {
    origin: corsWhitelist,
    credentials: true,
} satisfies CorsOptions;