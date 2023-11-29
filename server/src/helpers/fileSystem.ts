import path from 'path';

export function getFileURL(fromProjectDir: string): string {
  const projectDir = import.meta.url.split('/src')[0];

  let filePath = fromProjectDir.replace('@/', 'server/src/')
  let fullPath = new URL(filePath, projectDir).pathname;

  // On Windows, remove the leading slash before the drive letter
  if (process.platform === 'win32') {
    fullPath = fullPath.replace(/^\/(\w:)/, '$1');
  }

  return fullPath;
}