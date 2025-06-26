import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import termcolors

class Command(BaseCommand):
    help = 'Project cleanup and SQLite database reset'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput', '--no-input',
            action='store_false',
            dest='interactive',
            help='Run without confirmation',
        )

    def handle(self, *args, **options):
        success_style = termcolors.make_style(fg="green")
        running_style = termcolors.make_style(fg="blue", opts=("bold",))

        self.stdout.write(running_style("\n→ Cleaning up project..."))
        deleted_items = self.clean_project_files()
        
        if deleted_items["pycache"]:
            self.stdout.write(success_style(f"✔ Deleted __pycache__ folders ({deleted_items['pycache']} items)"))
        if deleted_items["migrations"]:
            self.stdout.write(success_style(f"✔ Deleted migrations folders ({deleted_items['migrations']} items)"))

        self.stdout.write(running_style("\n→ Cleaning up SQLite database..."))
        self.clean_sqlite(options['interactive'])

    def clean_project_files(self):
        target_dir = getattr(settings, 'BASE_DIR', '.')
        counters = {"pycache": 0, "migrations": 0}

        for root, dirs, _ in os.walk(target_dir):
            if 'env' in dirs:
                dirs.remove('env')
                
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if dir_name == "__pycache__":
                    shutil.rmtree(dir_path, ignore_errors=True)
                    counters["pycache"] += 1
                elif dir_name == "migrations":
                    shutil.rmtree(dir_path, ignore_errors=True)
                    counters["migrations"] += 1

        return counters
    
    def clean_sqlite(self, interactive):
        db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        if os.path.exists(db_path):
            if interactive:
                confirm = input('\nSQLite database will be deleted! Do you confirm? [y/N]: ')
                if confirm.lower() != 'y':
                    return
            os.remove(db_path)
            self.stdout.write(termcolors.make_style(fg="green")("✔ SQLite database deleted"))
        else:
            self.stdout.write(termcolors.make_style(fg="yellow")("ℹ No SQLite database found"))
