import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const project = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const checkout = process.env.EIDOS_REPO_DIR;
if (!checkout) {
  console.error("Set EIDOS_REPO_DIR to an Eidos checkout with Plugin API 1.6.0 tools.");
  process.exit(1);
}

const tool = path.join(path.resolve(checkout), "packages/plugin-tools/bin/eidos-plugin.mjs");
if (!existsSync(tool)) {
  console.error(`Plugin tools not found at ${tool}`);
  process.exit(1);
}

const result = spawnSync(process.execPath, [tool, ...process.argv.slice(2)], {
  cwd: project,
  stdio: "inherit",
});
if (result.error) throw result.error;
process.exit(result.status ?? 1);
