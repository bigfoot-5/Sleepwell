import click
from storage import upsert_log
from suggestion import generate_suggestions_for
from scoring import score_log_entry

@click.group()
def cli():
    pass

@cli.command()
@click.option('--user', required=True)
@click.option('--date', required=True)
@click.option('--took_tab1', type=bool, default=False)
@click.option('--took_tab2', type=bool, default=False)
@click.option('--took_tab3', type=bool, default=False)
@click.option('--caffeine', type=float, default=0.0)
@click.option('--alcohol', type=float, default=0.0)
@click.option('--workout', type=float, default=0.0)
@click.option('--nap', type=float, default=0.0)
@click.option('--mood', type=float, default=0.0)
@click.option('--sleep_time', type=float, default=0.0)
@click.option('--outdoor', type=float, default=0.0)
@click.option('--wakeups', type=int, default=0)
@click.option('--continuity', type=float, default=0.0)
def log(
    user, date, took_tab1, took_tab2, took_tab3,
    caffeine, alcohol, workout, nap, mood,
    sleep_time, outdoor, wakeups, continuity
):
    entry = {
        "user_id": user,
        "date": date,
        "took_tab1": took_tab1,
        "took_tab2": took_tab2,
        "took_tab3": took_tab3,
        "caffeine_intake_mg": caffeine,
        "alcohol_intake_units": alcohol,
        "workout_minutes": workout,
        "nap_duration_minutes": nap,
        "mood_rating": mood,
        "sleep_time_hours": sleep_time,
        "outdoor_activity_hours": outdoor,
        "wake_up_time": None,  # you can extend CLI to accept
        "number_of_wakeups": wakeups,
        "continuity_score": continuity,
        "sleep_score": None,
        "suggestions": []
    }
    upsert_log(entry)
    click.echo(f"Log entry saved for {user} {date}")

@cli.command()
@click.option('--user', required=True)
@click.option('--date', required=True)
def suggest(user, date):
    suggestion = generate_suggestions_for(user, date)
    click.echo("Suggestion: " + suggestion)

if __name__ == "__main__":
    cli()