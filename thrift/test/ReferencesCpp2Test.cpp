/*
 * Copyright 2016-present Facebook, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <thrift/test/gen-cpp2/References_types.h>
#include <thrift/test/gen-cpp2/References_types.tcc>
#include <thrift/lib/cpp2/protocol/Serializer.h>
#include <folly/portability/GTest.h>

using namespace apache::thrift;

namespace cpp2 {

TEST(References, recursive_ref_fields) {
  SimpleJSONProtocolWriter writer;
  folly::IOBufQueue buff;
  writer.setOutput(&buff, 1024);

  EXPECT_EQ(nullptr, buff.front());

  cpp2::RecursiveStruct a;
  // Normally non-optional fields are present in a default-constructed object,
  // here we check the special-case of a recursive data type with a non-optional
  // or even required reference to its own type: obviously this doesn't make a
  // lot of sense since any chain of such structure must either contain a cycle
  // (meaning we can't possibly serialize it) or a nullptr (meaning it's in fact
  // optional), but for historical reasons we allow this and default the
  // value to `nullptr`.
  EXPECT_EQ(nullptr, a.def_field.get());
  EXPECT_EQ(nullptr, a.req_field.get());
  // Check that optional fields are absent from a default-constructed object
  EXPECT_EQ(nullptr, a.opt_field.get());

  // this isn't the correct serialized size, but it's what simple json returns.
  // it is the correct length for a manually inspected, correct serializedSize
  EXPECT_EQ(120, a.serializedSize(&writer));
  EXPECT_EQ(120, a.serializedSizeZC(&writer));

  if (buff.front()) {
    EXPECT_EQ(0, buff.front()->length());
  }

  a.def_field = std::make_unique<cpp2::RecursiveStruct>();
  a.opt_field = std::make_unique<cpp2::RecursiveStruct>();
  EXPECT_EQ(415, a.serializedSize(&writer));
  EXPECT_EQ(415, a.serializedSizeZC(&writer));
}

TEST(References, ref_struct_fields) {
  ReferringStruct a;

  // tests that we initialize non-optional ref struct fields
  EXPECT_NE(nullptr, a.def_field);
  EXPECT_NE(nullptr, a.req_field);
  EXPECT_NE(nullptr, a.def_unique_field);
  EXPECT_NE(nullptr, a.req_unique_field);
  EXPECT_NE(nullptr, a.def_shared_field);
  EXPECT_NE(nullptr, a.req_shared_field);
  EXPECT_NE(nullptr, a.def_shared_const_field);
  EXPECT_NE(nullptr, a.req_shared_const_field);

  // Check that optional fields are absent from a default-constructed object
  EXPECT_EQ(nullptr, a.opt_field);
  EXPECT_EQ(nullptr, a.opt_unique_field);
  EXPECT_EQ(nullptr, a.opt_shared_field);
  EXPECT_EQ(nullptr, a.opt_shared_const_field);
}

TEST(References, ref_container_fields) {
  StructWithContainers a;

  // tests that we initialize non-optional ref container fields
  EXPECT_NE(nullptr, a.def_list_ref);
  EXPECT_NE(nullptr, a.def_set_ref);
  EXPECT_NE(nullptr, a.def_map_ref);
  EXPECT_NE(nullptr, a.def_list_ref_unique);
  EXPECT_NE(nullptr, a.def_set_ref_shared);
  EXPECT_NE(nullptr, a.def_list_ref_shared_const);
  EXPECT_NE(nullptr, a.req_list_ref);
  EXPECT_NE(nullptr, a.req_set_ref);
  EXPECT_NE(nullptr, a.req_map_ref);
  EXPECT_NE(nullptr, a.req_list_ref_unique);
  EXPECT_NE(nullptr, a.req_set_ref_shared);
  EXPECT_NE(nullptr, a.req_list_ref_shared_const);
  // Check that optional fields are absent from a default-constructed object
  EXPECT_EQ(nullptr, a.opt_list_ref);
  EXPECT_EQ(nullptr, a.opt_set_ref);
  EXPECT_EQ(nullptr, a.opt_map_ref);
  EXPECT_EQ(nullptr, a.opt_list_ref_unique);
  EXPECT_EQ(nullptr, a.opt_set_ref_shared);
  EXPECT_EQ(nullptr, a.opt_list_ref_shared_const);
}

} // namespace cpp2
