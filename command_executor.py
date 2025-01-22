import subprocess

class CommandExecutor:
    @staticmethod
    def run_command(command, cwd):
        try:
            res = subprocess.run(
                command, 
                cwd=cwd, 
                check=True, 
                text=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE
            )

            return {"success": True, "result": res.stdout}
        
        except subprocess.CalledProcessError as e:
            return {"success": False, "error": e.stderr}

