import { execSync } from 'child_process';

try {
  const zipPath = '/home/user/escortwp.zip';
  const extractDir = '/vercel/share/v0-project';
  console.log('[v0] Extracting from:', zipPath);
  execSync(`unzip -q "${zipPath}" -d "${extractDir}"`, { stdio: 'inherit' });
  console.log('[v0] Extraction complete');
} catch (error) {
  console.error('[v0] Error extracting:', error.message);
}
