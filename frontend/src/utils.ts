import camelCase from 'lodash-es/camelCase'
import mapKeys from 'lodash-es/mapKeys'
import capitalize from 'lodash-es/capitalize'
import format from 'date-fns/format'
import parseISO from 'date-fns/parseISO'
import { sl } from 'date-fns/locale'
import { Tweet, TweetType } from './types'

const RETWEET_PREFIX = 'RT '

// Determines type of tweet
export const getTweetType = (tweet: Tweet): TweetType => {
  if (tweet.text.startsWith(RETWEET_PREFIX)) {
    return TweetType.RETWEET
  } else if (tweet.quotedStatusId) {
    return TweetType.RETWEET_WITH_COMMENT
  } else {
    return TweetType.TWEET
  }
}

// Converts object keys to camelCase
export const keysToCamel = (object) => mapKeys(object, (_, k) => camelCase(k))

// Formats date a specific way used as title and social media share text
export const formatDate = (dateString: string): string =>
  capitalize(format(parseISO(dateString), 'EEEE, d. MMMM y', { locale: sl }))

export const formatDateMobile = (dateString: string): string =>
  capitalize(format(parseISO(dateString), 'EEEE, d. M. y', { locale: sl }))

// Calculates hours and minutes from seconds
export const formatSeconds = (
  seconds: number
): { hours: number; minutes: number } => {
  const tweetTimeInMinutes = Math.round(seconds / 60)

  const hours = Math.floor(tweetTimeInMinutes / 60)
  const minutes = tweetTimeInMinutes % 60

  return { hours, minutes }
}
