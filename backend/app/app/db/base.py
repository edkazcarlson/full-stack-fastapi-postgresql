# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.club import Club, ClubMember, ClubRole
from app.models.calendarEvents import CalendarEvents
from app.models.forum import Forum, ForumChannel, ForumFolder, ForumPost
# from app.models.demo import Parent, Child, AssocTable