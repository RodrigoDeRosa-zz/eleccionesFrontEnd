from src.util.DateUtils import DateUtils


class CandidatesResponseMapper:

    @classmethod
    def map_many(cls, documents):
        """ The result is a list of objects which have a date and a map that associates candidate name and the increases
        on that date. """
        by_date = {}
        # Rename _id field for every document and map date to timestamp
        for document in documents:
            screen_name = document['_id']
            increases = [{'count': increase['count'], 'date': increase['date'].date()}
                         for increase in document['increases']]
            for increase in increases:
                cls.__add_to_dictionary_map(by_date, increase['date'], screen_name, increase['count'])
        return [cls.__make_date_dict(key, value) for key, value in by_date.items()]

    @staticmethod
    def __add_to_dictionary_map(dictionary, key, map_key, map_value):
        """ Add an element to the set of a certain key in a dictionary of lists """
        if key not in dictionary.keys():
            dictionary[key] = dict()
        dictionary[key][map_key] = map_value

    @staticmethod
    def __make_date_dict(key, value):
        """ Create a dictionary adding first entry {'date': key} and flatten value, which is a map. """
        dictionary = {'date': DateUtils.date_to_timestamp(key)}
        for screen_name, count in value.items():
            dictionary[screen_name] = count
        return dictionary
