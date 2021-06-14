import { GetServerSideProps, NextPage } from 'next'
import Head from 'next/head'
import classnames from 'classnames'

import { Container, Breadcrumbs, Link, Typography } from '@material-ui/core'

import { Translation, Project, Language } from '../../../src/global.types'
import { getProject, getProjects } from '../../../src/api/projects'
import TranslationField from '../../../src/components/TranslationField'
import { getTranslations } from '../../../src/api/translations'
import joinTranslations, {
  JoinedTranslation,
} from '../../../src/utils/joinTranslations'

import style from './[language_code].module.css'

/**
 * Translations Page - Page for viewing and editing translations
 */

interface StaticProps {
  project: Project
  translations: Translation[]
  englishTranslations: Translation[]
  joinedTranslations: JoinedTranslation[]
  selectedLanguage: Language
}


export const getServerSideProps: GetServerSideProps<
  StaticProps,
  { id: string; language_code: string }
> = async ({ params }) => {
  const project = await getProject(params.id)

  const selectedLanguage = project.languages.find(
    (language) => language.language_code === params.language_code
  )
  const english = project.languages.find(
    (language) => language.language_code === 'en'
  )

  const translations = await getTranslations(
    parseInt(params.id),
    selectedLanguage.id
  )
  const englishTranslations = await getTranslations(
    parseInt(params.id),
    english.id
  )

  const unsortedJoinedTranslations = joinTranslations(
    englishTranslations,
    translations
  )

  const emptyTranslations = unsortedJoinedTranslations.filter(
    (translation) => !translation.selected?.text
  )
  const filledTranslations = unsortedJoinedTranslations.filter(
    (translation) => translation.selected?.text ?? false
  )

  return {
    props: {
      project,
      translations,
      englishTranslations,
      joinedTranslations: [...emptyTranslations, ...filledTranslations],
      selectedLanguage,
    },
  }
}

const ProjectPage: NextPage<StaticProps> = ({
  project,
  selectedLanguage,
  joinedTranslations,
}) => {
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta name="description" content="Editing translations" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container style={{ marginTop: 20, marginBottom: 20 }} maxWidth="xl">
          <Breadcrumbs style={{ marginBottom: 20 }} aria-label="breadcrumb">
            <Link color="inherit" href="/">
              Projects
            </Link>
            <Link color="inherit" href={`/projects/${project.id}/`}>
              {project.name}
            </Link>
            <Typography color="textPrimary">{selectedLanguage.name}</Typography>
          </Breadcrumbs>
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'auto 1fr 1fr',
              gridTemplateRows: 'auto',
              alignItems: 'center',
            }}
          >
            <div className={classnames(style.gridCell, style.gridHeaderCell)}>
              <b>
                <code>Dotpath</code>
              </b>
            </div>
            <div className={classnames(style.gridCell, style.gridHeaderCell)}>
              <b>English</b>
            </div>
            <div className={classnames(style.gridCell, style.gridHeaderCell)}>
              <b>{selectedLanguage.name}</b>
            </div>

            {joinedTranslations.map((joinedTranslation) => {
              return (
                <>
                  <div className={style.gridCell}>
                    <code>{joinedTranslation.english.dotpath}</code>
                  </div>
                  <div className={style.gridCell}>
                    <span style={{ whiteSpace: 'pre-line', fontSize: '1rem' }}>
                      {joinedTranslation.english.text}
                    </span>
                  </div>
                  <div className={style.gridCell}>
                    <TranslationField
                      base={joinedTranslation.english}
                      selected={joinedTranslation.selected}
                      language={selectedLanguage}
                    />
                  </div>
                </>
              )
            })}
          </div>
        </Container>
      </main>
    </div>
  )
}

export default ProjectPage
