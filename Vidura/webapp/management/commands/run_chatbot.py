from django.core.management.base import BaseCommand
from Vidura.webapp import chatbot


class Command(BaseCommand):
    help = 'Runs the conversation simulations with GPT for favorite foods.'

    def add_arguments(self, parser):
        parser.add_argument("-n", nargs="?", default=100, type=int,
                            help="Number of simulations to run",)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting simulation of {n} conversations...'))

        for i in range(options['n']):
            self.stdout.write(f"\n--- Running Conversation {i + 1}/{options['n']} ---")
            try:
                chatbot.run_conversation()
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"An error occurred during conversation {i + 1}: {e}"))

        self.stdout.write(self.style.SUCCESS('\nSimulation complete.'))
