# Copyright 2023 The Orbax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Shorthand for `Checkpointer(PyTreeCheckpointHandler())`."""

from typing import Any, Optional
from etils import epath
from orbax.checkpoint import abstract_checkpointer
from orbax.checkpoint import checkpointer
from orbax.checkpoint import pytree_checkpoint_handler


class PyTreeCheckpointer(abstract_checkpointer.AbstractCheckpointer):
  """Shorthand class.

  Instead of::
    ckptr = Checkpointer(PyTreeCheckpointHandler())

  we can use::
    ckptr = PyTreeCheckpointer()
  """

  def __init__(self, primary_host: int = 0):
    self._checkpointer = checkpointer.Checkpointer(
        pytree_checkpoint_handler.PyTreeCheckpointHandler(),
        primary_host=primary_host,
    )

  def save(
      self, directory: epath.PathLike, item: Any, *args: Any, **kwargs: Any
  ):
    return self._checkpointer.save(directory, item, *args, **kwargs)

  def restore(
      self,
      directory: epath.PathLike,
      *args: Any,
      item: Optional[Any] = None,
      **kwargs: Any
  ) -> Any:
    return self._checkpointer.restore(directory, *args, item=item, **kwargs)

  def metadata(self, directory: epath.PathLike) -> Optional[Any]:
    """See superclass documentation."""
    return self._checkpointer.metadata(directory)

  def close(self):
    self._checkpointer.close()
