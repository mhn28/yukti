import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      external: [
        "@tauri-apps/api",
        "@tauri-apps/api/core"
      ]
    }
  }
});
