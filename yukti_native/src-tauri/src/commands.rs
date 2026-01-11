use std::process::Command;

#[tauri::command]
pub fn run_assistant(payload: String) -> String {
    println!("RUST RECEIVED PAYLOAD: {}", payload);

    let output = Command::new("python3")
        .arg("../../yukti/api/ui_bridge.py")
        .arg(payload)
        .output();

    match output {
        Ok(out) => String::from_utf8_lossy(&out.stdout).to_string(),
        Err(e) => format!("Rust execution error: {}", e)
    }
}
