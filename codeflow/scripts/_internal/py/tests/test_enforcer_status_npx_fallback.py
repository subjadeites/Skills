import json
import os
import stat
import subprocess
import tempfile
import unittest


SCRIPT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BIN_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "bin"))
ENFORCER = os.path.join(BIN_DIR, "enforcer.sh")


def _write_executable(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR)


class EnforcerStatusNpxFallbackTests(unittest.TestCase):
    def test_status_exposes_install_button_when_only_npx_is_available(self):
        with tempfile.TemporaryDirectory() as td:
            fake_bin = os.path.join(td, "bin")
            os.makedirs(fake_bin, exist_ok=True)

            _write_executable(
                os.path.join(fake_bin, "npx"),
                "#!/bin/sh\nexit 0\n",
            )

            env = dict(os.environ)
            env["PATH"] = fake_bin + os.pathsep + env.get("PATH", "")

            proc = subprocess.run(
                ["/bin/bash", ENFORCER, "status", "--json"],
                capture_output=True,
                text=True,
                env=env,
            )

            self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
            payload = json.loads(proc.stdout)
            self.assertTrue(payload["openclawCli"])
            self.assertEqual(payload["openclawLauncherKind"], "npx")
            self.assertTrue(payload["canInstall"])
            self.assertEqual(payload["recommendation"]["action"], "install")
            self.assertTrue(payload["recommendation"]["buttons"])
            self.assertEqual(payload["recommendation"]["callbackData"], "cfe:install")


if __name__ == "__main__":
    unittest.main()
