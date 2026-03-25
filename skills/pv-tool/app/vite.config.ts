import { defineConfig } from 'vite';
import FullReload from 'vite-plugin-full-reload';

export default defineConfig({
  base: process.env.VITE_BASE ?? '/pv-tool/',
  plugins: [
    FullReload(['src/**/*']),
  ],
});
