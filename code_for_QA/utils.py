
step_phase_mapping = {  # all lower case
    'nasal_corridor_creation': 'nasal_sphenoid',
    'anterior_sphenoidotomy': 'nasal_sphenoid',
    'septum_displacement': 'nasal_sphenoid',
    'sphenoid_sinus_clearance': 'nasal_sphenoid',
    'sellotomy': 'sellar',
    'durotomy': 'sellar',
    'tumour_excision': 'sellar',
    'haemostasis': 'closure',
    'synthetic_graft_placement': 'closure',
    'fat_graft_placement': 'closure',
    'gasket_seal_construct': 'closure',
    'dural_sealant': 'closure',
    'nasal_packing': 'closure',
    'debris_clearance': 'closure',
    'operation_not_started': 'UNDEFINED PHASE: the step is not 1 of 14 steps',  # invalid result
    'operation_ended': 'UNDEFINED PHASE: the step is not 1 of 14 steps',  # invalid result
    'out_of_patient': 'UNDEFINED PHASE: the step is not 1 of 14 steps',  # invalid result
}

next_step_mapping = {  # all lower case
    'nasal_corridor_creation': 'anterior_sphenoidotomy',
    'anterior_sphenoidotomy': 'septum_displacement',
    'septum_displacement': 'sphenoid_sinus_clearance',
    'sphenoid_sinus_clearance': 'sellotomy',
    'sellotomy': 'durotomy',
    'durotomy': 'tumour_excision',
    'tumour_excision': 'haemostasis',
    'haemostasis': 'synthetic_graft_placement',
    'synthetic_graft_placement': 'fat_graft_placement',
    'fat_graft_placement': 'gasket_seal_construct',
    'gasket_seal_construct': 'dural_sealant',
    'dural_sealant': 'nasal_packing',
    'nasal_packing': 'debris_clearance',
    'debris_clearance': 'end_of_step',
    'operation_not_started': 'Current step is operation_not_started',  # invalid result
    'operation_ended': 'Current step is operation_ended',  # invalid result
    'out_of_patient': 'Current step is out_of_patient',  # invalid result
}

next_phase_mapping = {
    'nasal_sphenoid': 'sellar',
    'sellar': 'closure',
    'closure': 'end_of_phase',
    'UNDEFINED PHASE: the step is not 1 of 14 steps': 'Invalid current phase'  # invalid result
}

step_operation_mapping = {
    'nasal_corridor_creation': 'The middle and superior turbinates are laterally displaced',
    'anterior_sphenoidotomy': 'The sphenoid ostium is identified and opened',
    'septum_displacement': 'The septum is displaced until the opposite ostium is seen',
    'sphenoid_sinus_clearance':
        'The sphenoid sinus is opened, with removal of sphenoid septations to expose the face of the sella and mucosa',
    'sellotomy': 'The sella is identified, confirmed and carefully opened',
    'durotomy': 'A cruciate durotomy is performed',
    'tumour_excision': 'The tumour is seen and removed in a piecemeal fashion',
    'haemostasis': 'Haemostasis is achieved with a surgiflo, a bipolar cautery, and a spongostan placement',
    'synthetic_graft_placement': 'spongostan, tachosil and duragen placement',
    'fat_graft_placement': 'A fat graft is placed over the defact',
    'gasket_seal_construct': 'A MedPor implant and a fascia lata graft are placed',
    'dural_sealant': 'Evicel and Adherus dural sealant are applied',
    'nasal_packing': 'The nasal cavity is packed with Bismuth soaked ribbon gauze',
    'debris_clearance': 'Debris is cleared from the nasal cavity and choana',
    'operation_not_started': 'UNDEFINED OPERATION',  # invalid result
    'operation_ended': 'UNDEFINED OPERATION',  # invalid result
    'out_of_patient': 'UNDEFINED OPERATION',  # invalid result
}

number_location_mapping = {  # float64 in excel
    '1.0': 'top-left',
    '2.0': 'top-right',
    '3.0': 'centre',
    '4.0': 'bottom-left',
    '5.0': 'bottom-right',
}

