import { defineConfig } from 'tsup';

export default defineConfig(() => ({
  entry: ['ts/client/src'],
  format: ['esm', 'cjs'],
  splitting: true,
  sourcemap: true,
  minify: false,
  clean: true,
  skipNodeModulesBundle: true,
  dts: true,
  external: ['node_modules'],
}));
