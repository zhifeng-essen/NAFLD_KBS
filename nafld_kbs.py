from PIL import Image
import json
import streamlit as st
import pandas as pd

import warnings
def warn(*args, **kwargs): pass
warnings.warn = warn

from nafld_kbs_nav import nafld_kbs_nav
from nafld_kbs_card import nafld_kbs_card
from nafld_kbs_search import nafld_kbs_search
from nafld_kbs_table import nafld_kbs_table
from ketcher import ketcher

icon = Image.open('./icon.png')
st.set_page_config(
    page_title='NAFLD KBS', 
    layout='wide',
    page_icon=icon, 
    menu_items={}
)

@st.cache
def read_data():
    clinical_trials = pd.read_excel('./data/Clinical_Trials.xlsx').set_index('Trial_ID')
    drugs = pd.read_excel('./data/Drugs.xlsx').set_index('Drug_ID')
    targets = pd.read_excel('./data/Therapy_Targets.xlsx').set_index('Target_ID')
    return clinical_trials, drugs, targets

clinical_trials, drugs, targets = read_data()


def trial_format(selected_trial):
    # Basic Information
    st.markdown("**Title**")
    st.markdown(selected_trial['Title'])

    st.markdown("**Source ID**")
    st.markdown("[{id}](https://ClinicalTrials.gov/show/{id})".format(
        id=selected_trial['Source_ID']
    ))

    st.markdown("**Acronym**")
    st.markdown(selected_trial['Acronym'])

    st.markdown("**Sponsor/Collaborators**")
    st.markdown(selected_trial['Sponsor/Collaborators'])

    st.markdown("**Locations**")
    st.markdown(selected_trial['Locations'])
    st.markdown("---")

    # Study Description
    st.markdown("**Conditions**")
    st.markdown(selected_trial['Conditions'])

    st.markdown("**Interventions**")
    st.markdown(selected_trial['Interventions'])

    st.markdown("**Phases**")
    st.markdown(selected_trial['Phases'])
    st.markdown("---")

    # Tracking Information
    st.markdown("**Status**")
    st.markdown(selected_trial['Status'])

    st.markdown("**Start Date**")
    st.markdown(selected_trial['Start Date'])

    st.markdown("**Completion Date**")
    st.markdown(selected_trial['Completion Date'])

    st.markdown("**Results First Posted**")
    st.markdown(selected_trial['Results First Posted'])

    st.markdown("**Last Update Posted**")
    st.markdown(selected_trial['Last Update Posted'])

    st.markdown("**Study Results**")
    st.markdown(selected_trial['Study Results'])

    st.markdown("**Results URL**")
    st.markdown(selected_trial['Results URL'])
    st.markdown("---")
    # Study Design
    st.markdown("**Study Type**")
    st.markdown(selected_trial['Study Type'])

    st.markdown("**Enrollment**")
    st.markdown(selected_trial['Enrollment'])

    st.markdown("**Study Designs**")
    st.markdown(selected_trial['Study Designs'])

    st.markdown("**Gender**")
    st.markdown(selected_trial['Gender'])

    st.markdown("**Age**")
    st.markdown(selected_trial['Age'])
    st.markdown("---")
    # Outcome Measures
    st.markdown("**Outcome Measures**")
    st.markdown(selected_trial['Outcome Measures'])
    st.markdown("---")
    # Others
    st.markdown("**Update**")
    st.markdown(selected_trial['Update'])


def drug_format(selected_drug):
    st.markdown("**Drug_Name**")
    st.markdown(selected_drug["Drug_Name"])
    st.markdown("**Synonyms**")
    st.markdown(selected_drug["Synonyms"])
    st.markdown("**Drug_Type**")
    st.markdown(selected_drug["Drug_Type"])
    st.markdown("**DrugBank_ID**")
    st.markdown("[{id}](https://go.drugbank.com/drugs/{id})".format(
        id=selected_drug["DrugBank_ID"]
    ))
    st.markdown("**DrugBank_Description**")
    st.markdown(selected_drug["DrugBank_Description"])
    st.markdown("**PubChem_ID**")
    st.markdown(selected_drug["PubChem_ID"])
    st.markdown("**CasNo**")
    st.markdown(selected_drug["CasNo"])
    st.markdown("**Repositioning for NAFLD**")
    st.markdown(selected_drug["Repositioning for NAFLD"])
    st.markdown("**SMILES**")
    st.markdown(selected_drug["SMILES"])
    st.markdown("**InChiKey**")
    st.markdown(selected_drug["InChiKey"])
    st.markdown("**Molecular_Weight**")
    st.markdown(selected_drug["Molecular_Weight"])
    st.markdown("**DrugBank_Targets**")
    st.markdown(selected_drug["DrugBank_Targets"])
    st.markdown("**DrugBank_MoA**")
    st.markdown(selected_drug["DrugBank_MoA"])
    st.markdown("**DrugBank_Pharmacology**")
    st.markdown(selected_drug["DrugBank_Pharmacology"])
    st.markdown("**DrugBank_Indication**")
    st.markdown(selected_drug["DrugBank_Indication"])
    st.markdown("**Targets**")
    st.markdown(selected_drug["Targets"])
    st.markdown("**Therapeutic_Category**")
    st.markdown(selected_drug["Therapeutic_Category"])
    st.markdown("**Clinical_Trial_Progress**")
    st.markdown(selected_drug["Clinical_Trial_Progress"])
    st.markdown("**Latest_Progress**")
    st.markdown(selected_drug["Latest_Progress"])
    st.markdown("**Update**")
    st.markdown(selected_drug["Update"])


def target_format(selected_target):
    st.markdown("**Target_Name**")
    st.markdown(selected_target["Target_Name"])
    st.markdown("**Synonyms**")
    st.markdown(selected_target["Synonyms"])
    st.markdown("**Target_GENE**")
    st.markdown(selected_target["Target_GENE"])
    st.markdown("**Target_Action**")
    st.markdown(selected_target["Target_Action"])
    st.markdown("**Target_Class**")
    st.markdown(selected_target["Target_Class"])
    st.markdown("**Therapy_Drugs**")
    st.markdown(selected_target["Therapy_Drugs"])
    st.markdown("**UniProtKB_ID**")
    st.markdown(selected_target["UniProtKB_ID"])
    st.markdown("**UniProtKB_Entry_Name**")
    st.markdown(selected_target["UniProtKB_Entry_Name"])
    st.markdown("**Mechanism**")
    st.markdown(selected_target["Mechanism"])
    st.markdown("**Reference_PMIDs**")
    st.markdown(selected_target["Reference_PMIDs"])
    st.markdown("**ChEMBL_ID**")
    st.markdown("[{id}](https://www.ebi.ac.uk/chembl/target_report_card/{id})".format(
        id=selected_target["ChEMBL_ID"]
    ))
    st.markdown(selected_target["ChEMBL_ID"])
    st.markdown("**Update**")
    st.markdown(selected_target["Update"])


class MultiPage:
    def __init__(self) -> None:
        self.header = st.empty()
        self.body = st.empty()
        self.footer = st.empty()
        session_init = [('nav_click_time', 0), ('current_page', 'home'), ('item_id', 0)]
        for key, value in session_init:
            st.session_state[key] = value

    def update_session_from_link(self):
        for key, value in st.experimental_get_query_params().items():
            st.session_state[key] = value[0]

    def set_link(self, params):
        st.experimental_set_query_params(**params)

    def navigation(self, nav_click_time):
        with self.header:
            # Custom navbar component
            nav_component_value = nafld_kbs_nav(nav_click_time=nav_click_time)
            if not nav_component_value == 0:
                if int(nav_component_value['nav_click_time']) != int(st.session_state.nav_click_time):
                    self.set_link({
                        'nav_click_time': nav_component_value['nav_click_time'],
                        'current_page': nav_component_value['current_page'],
                        'item_id': 0
                    })
                    st.experimental_rerun()

    def search(self):
        query_type = st.session_state.query_type
        query = st.session_state.query
        if query_type == 'trial': # Trial search 
            res = clinical_trials[
                clinical_trials["Source_ID"].str.contains(query, case=False, na=False) +
                clinical_trials["Title"].str.contains(
                    query, case=False, na=False)
            ]
            res_data = {'type': 'trials', 'data': []}
            for i in res.index:
                tmp = json.loads(clinical_trials.loc[i].to_json())
                tmp['Trial_ID'] = i
                res_data['data'].append(tmp)
        elif query_type == 'drug': # Drug search
            res = drugs[
                drugs["Drug_Name"].str.contains(query, case=False, na=False) +
                drugs["DrugBank_ID"].str.contains(query, case=False, na=False)
            ]
            res_data = {'type': 'drugs', 'data': []}
            for i in res.index:
                tmp = json.loads(drugs.loc[i].to_json())
                tmp['Drug_ID'] = i
                res_data['data'].append(tmp)
        elif query_type == 'target': # target search
            res = targets[
                targets["Target_Name"].str.contains(query, case=False, na=False) +
                targets["Target_GENE"].str.contains(
                    query, case=False, na=False)
            ]
            res_data = {'type': 'targets', 'data': []}
            for i in res.index:
                tmp = json.loads(targets.loc[i].to_json())
                tmp['Target_ID'] = i
                res_data['data'].append(tmp)
        elif query_type == 'smiles': # TO DO: Structure search
            res = drugs[
                drugs["SMILES"].str.contains(query, case=False, na=False)
            ]
            res_data = {'type': 'drugs', 'data': []}
            for i in res.index:
                tmp = json.loads(drugs.loc[i].to_json())
                tmp['Drug_ID'] = i
                res_data['data'].append(tmp)

        return res_data

    def page_home(self):
        with st.container():
            
            # st.markdown("<label>🔍  BASIC SEARCH</label>", unsafe_allow_html=True)
            # Basic Search
            basic_search = nafld_kbs_search(
                name="basic_search", key="basic_search")
            if basic_search:
                self.set_link({
                    'nav_click_time': st.session_state.nav_click_time,
                    'current_page': "search_results",
                    'query_type': basic_search['query_type'],
                    'query': basic_search['query'],
                    'item_id': 0
                })
                st.experimental_rerun()
            # Custom card component for statistics
            st.markdown("<label>📊  STATISTICS</label>", unsafe_allow_html=True)
            nafld_kbs_card(items=[{
                'name': 'Clinical Trials',
                'value': 'trials',
                'number': clinical_trials.shape[0],
                'icon': 'mdi-ab-testing'
            }, {
                'name': 'Drugs',
                'value': 'drugs',
                'number': drugs.shape[0],
                'icon': 'mdi-pill'
            }, {
                'name': 'Therapy Targets',
                'value': 'targets',
                'number': targets.shape[0],
                'icon': 'mdi-dna'
            }])
            # Structure Search
            st.markdown("<label>🔍  STRUCTURE SEARCH</label>", unsafe_allow_html=True)
            smiles = ketcher(name="structure_search", key="structure_search")
            if smiles:
                self.set_link({
                    'nav_click_time': st.session_state.nav_click_time,
                    'current_page': "search_results",
                    'query_type': 'smiles',
                    'query': smiles,
                    'item_id': 0
                })
                st.experimental_rerun()

    def page_search_results(self):
        with st.container():
            st.markdown(
                "<label>🔎  %s SEARCH RESULTS FOR: '%s' </label>" % (st.session_state.query_type.upper(), st.session_state.query.upper()), 
                unsafe_allow_html=True
            )
            res_data = self.search()
            nafld_kbs_table(res_data)

    def page_trials(self):
        with st.container():
            st.markdown("<label>💉  CLINICAL TRIALS</label>", unsafe_allow_html=True)
            clinical_trials_data = {'type': 'trials', 'data': []}
            for i in clinical_trials.index:
                tmp = json.loads(clinical_trials.loc[i].to_json())
                tmp['Trial_ID'] = i
                clinical_trials_data['data'].append(tmp)
            nafld_kbs_table(clinical_trials_data)

    def page_trial_details(self):
        trial_id = st.session_state.item_id
        with st.container():
            trial_format(clinical_trials.loc[int(trial_id)].to_dict())

    def page_drugs(self):
        with st.container():
            st.markdown("<label>💊  DRUGS</label>", unsafe_allow_html=True)
            drugs_data = {'type': 'drugs', 'data': []}
            for i in drugs.index:
                tmp = json.loads(drugs.loc[i].to_json())
                tmp['Drug_ID'] = i
                drugs_data['data'].append(tmp)
            nafld_kbs_table(drugs_data)

    def page_drug_details(self):
        drug_id = st.session_state.item_id
        with st.container():
            drug_format(drugs.loc[int(drug_id)].to_dict())

    def page_targets(self):
        with st.container():
            st.markdown("<label>🧬  TARGETS</label>", unsafe_allow_html=True)
            targets_data = {'type': 'targets', 'data': []}
            for i in targets.index:
                tmp = json.loads(targets.loc[i].to_json())
                tmp['Target_ID'] = i
                targets_data['data'].append(tmp)
            nafld_kbs_table(targets_data)

    def page_target_details(self):
        target_id = st.session_state.item_id
        with st.container():
            target_format(targets.loc[int(target_id)].to_dict())

    def page_about(self):
        st.info('This is About')

    def run(self):
        self.update_session_from_link()
        self.navigation(st.session_state.nav_click_time)
        self.body.empty()
        with self.body:
            if st.session_state.current_page == 'home':
                self.page_home()
            elif st.session_state.current_page == 'search_results':
                self.page_search_results()
            elif st.session_state.current_page == 'trials':
                self.page_trials()
            elif st.session_state.current_page == 'trial_details':
                self.page_trial_details()
            elif st.session_state.current_page == 'drugs':
                self.page_drugs()
            elif st.session_state.current_page == 'drug_details':
                self.page_drug_details()
            elif st.session_state.current_page == 'targets':
                self.page_targets()
            elif st.session_state.current_page == 'target_details':
                self.page_target_details()
            elif st.session_state.current_page == 'about':
                self.page_about()
            else:
                self.page_home()

        self.set_link({
            'nav_click_time': st.session_state.nav_click_time,
            'current_page': st.session_state.current_page,
            'item_id': st.session_state.item_id
        })


app = MultiPage()
app.run()

# st.write(st.session_state)
st.markdown("""
<style>
    .block-container {
        max-width: 84%;
        padding-top: 1rem;
    }
    header {
        visibility: hidden;
        height: 0;
    }
    footer {
        visibility: hidden;
        height: 0;
    }
    label {
        font-size: 24px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)
