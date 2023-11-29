export { };

declare global {

  /**
   * @property MAIN_IP: string
   * @property PORT_BACK: number
   * @property PORT_FRONT: number
   * @property UNREAL_IP: string
   * @property UNREAL_OSC_PORT: number
   * @property UNREAL_HTTP_PORT: number
   * @property MARGIN_X: number
   * @property MARGIN_Y: number
   * @property OFFSET_X: number
   * @property OFFSET_Y: number
   * @property DETECTION_CONFIDENCE: number
   * @property TRACKING_CONFIDENCE: number
   * @property OS_TYPE: string
   */
  interface Configs{

    MAIN_IP: string;
    PORT_BACK: number;
    PORT_FRONT: number;
    PORT_FRONT_DEV: number;
    UNREAL_IP: string;
    UNREAL_OSC_PORT: number;
    UNREAL_HTTP_PORT: number;

    MARGIN_X: number;
    MARGIN_Y: number;
    OFFSET_X: number;
    OFFSET_Y: number;
    DETECTION_CONFIDENCE: number;
    TRACKING_CONFIDENCE: number;
    
    OS_TYPE: string;
  }
}