from flask_restful import Resource

from src.db.daos.CooccurrenceDAO import CooccurrenceDAO
from src.db.daos.CooccurrenceGraphDAO import CooccurrenceGraphDAO
from src.db.daos.HashtagDAO import HashtagDAO
from src.db.daos.RawFollowerDAO import RawFollowerDAO
from src.db.daos.RawTweetDAO import RawTweetDAO
from src.services.CandidateService import CandidateService
from src.util.ResponseBuilder import ResponseBuilder


class DashboardResource(Resource):

    @staticmethod
    def get():
        # Get count of analyzed tweets
        tweets = RawTweetDAO().get_count({})
        # Get total count of users
        users = RawFollowerDAO().get_count({})
        # Get count of active users
        active_users = RawFollowerDAO().get_count({'has_tweets': True})
        # Get count of followers for each candidate
        candidates = list(map(lambda c: c.screen_name, CandidateService().get_all()))
        followers_by_candidate = dict()
        for candidate in candidates:
            followers = RawFollowerDAO().get_count({'follows': candidate})
            active_followers = RawFollowerDAO().get_count({'follows': candidate, 'has_tweets': True})
            followers_by_candidate[candidate] = {'followers': followers,
                                                 'active_followers': active_followers,
                                                 'proportion': active_followers / followers}
        # Get count of found topics
        topics = CooccurrenceGraphDAO().get_count({'topic_id': {'$ne': 'main'}})
        # Get count of known hashtags
        hashtags = HashtagDAO().get_count({})
        # Get count of hashtag cooccurrences
        cooccurrences = CooccurrenceDAO().get_count({})
        # Build response object
        response = {'tweets': tweets,
                    'total_users': users,
                    'active_users': active_users,
                    'active_proportion': active_users / users,
                    'followers_by_candidate': followers_by_candidate,
                    'topic_count': topics,
                    'hashtag_count': hashtags,
                    'cooccurrences_count': cooccurrences}
        # Respond request
        return ResponseBuilder.build(response, 200)
