from cride.circles.models import Circle
import csv

def import_data(file):
    with open(file, 'r') as f:
        content = list(csv.reader(f))
        # print(f)
        for circle in content[1:]:
            Circle(name=circle[0],
                slug_name=circle[1],
                is_public=circle[2],
                verified=circle[3],
                members_limit=circle[4]
            ).save()
