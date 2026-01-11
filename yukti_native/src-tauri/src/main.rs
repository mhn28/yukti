#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]


mod commands;
use commands::run_assistant;


use tauri::command;

#[command]
fn assistant_query(query: String) -> String {
    format!(
        "Yukti Assistant (native):\n\nReceived query:\n{}\n\nNext phase will route this to Python core.",
        query
    )
}

fn main() {
    tauri::Builder::default()
    .invoke_handler(tauri::generate_handler![run_assistant])

        .invoke_handler(tauri::generate_handler![assistant_query])
        .run(tauri::generate_context!())
        .expect("error while running Yukti");
}
