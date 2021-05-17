import { Translation } from '../global.types'
import fetchWrapper from './fetchWrapper'

export const getTranslations = async (
  project_id: number | string,
  language_id: number | string
): Promise<Translation[]> => {
  return fetchWrapper({
    url: `http://localhost:8000/translations/?project=${project_id}&language=${language_id}`,
  })
}
