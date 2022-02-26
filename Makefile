build:
	docker-compose -f docker-compose-loc.yml build

up:
	docker-compose -f docker-compose-loc.yml up

superuser:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py createsuperuser


shell:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py shell

export_data:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py dumpdata --indent 4 > fixture.json

import_data:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py loaddata fixture.json

migrate:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py makemigrations
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py migrate

clean_data: export_data
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py flush

test:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py test --no-input --parallel

app:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py startapp $(name)


statics:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py collectstatic --no-input

messages:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py makemessages -l 'es'
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py makemessages -l 'en'

compilemessages:
	docker-compose -f docker-compose-loc.yml run --rm django python manage.py compilemessages -f

pylint:
	docker-compose -f docker-compose-loc.yml run --rm django bash -c './pylint.sh'

django:
	docker-compose -f docker-compose-loc.yml restart django

stop:
	docker-compose -f docker-compose-loc.yml stop