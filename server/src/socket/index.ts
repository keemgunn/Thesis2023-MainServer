import { Server } from 'socket.io';
import https from 'https';
import { corsOptions } from '../helpers/cors.js';

export function createSocket(server: https.Server) {
  const io = new Server(server, {
    cors: corsOptions,
  });

  return {
    io
  }
}