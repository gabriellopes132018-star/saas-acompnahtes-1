import { execSync } from 'child_process';

try {
  execSync('cd /vercel/share/v0-project && unzip -q escortwp.zip', { stdio: 'inherit' });
  console.log('[v0] Extraction complete');
} catch (error) {
  console.error('[v0] Error extracting:', error.message);
}
