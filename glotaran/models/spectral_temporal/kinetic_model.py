"""Glotaran Kinetic Model"""

from glotaran.model import model, BaseModel

from .initial_concentration import InitialConcentration
from .irf import Irf
from .k_matrix import KMatrix
from .kinetic_fit_result import KineticFitResult
from .kinetic_megacomplex import KineticMegacomplex
from .spectral_constraints import SpectralConstraint
from .spectral_relations import SpectralRelation
from .spectral_shape import SpectralShape
from .spectral_temporal_dataset_descriptor import SpectralTemporalDatasetDescriptor
from .kinetic_matrix import calculate_kinetic_matrix
from .spectral_matrix import calculate_spectral_matrix


@model(
    'kinetic',
    attributes={
        'initial_concentration': InitialConcentration,
        'k_matrix': KMatrix,
        'irf': Irf,
        'shape': SpectralShape,
        'spectral_constraints': SpectralConstraint,
        'spectral_relations': SpectralRelation,
    },
    dataset_type=SpectralTemporalDatasetDescriptor,
    megacomplex_type=KineticMegacomplex,
    calculated_matrix=calculate_kinetic_matrix,
    calculated_axis='time',
    estimated_matrix=calculate_spectral_matrix,
    estimated_axis='spectral',
    fit_result_class=KineticFitResult
)
class KineticModel(BaseModel):
    """A kinetic model is an implementation for model.Model. It is used describe
    time dependend datasets.

    """
