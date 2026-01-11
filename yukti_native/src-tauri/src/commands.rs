use std::process::{Command, Stdio};
use std::io::Write;

#[tauri::command]
pub fn run_assistant(query: String) -> Result<String, String> {
    let mut child = Command::new("python")
        .arg("-m")
        .arg("yukti.api.assistant_entry")
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .spawn()
        .map_err(|e| e.to_string())?;

    if let Some(stdin) = child.stdin.as_mut() {
        stdin.write_all(query.as_bytes()).map_err(|e| e.to_string())?;
    }

    let output = child.wait_with_output().map_err(|e| e.to_string())?;
    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}
